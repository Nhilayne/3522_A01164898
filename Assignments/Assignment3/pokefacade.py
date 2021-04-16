from request import Request
import aiohttp
import asyncio
import os
from pokeretriever.pokedata import Ability, Move, Pokemon, Stats


class PokeFacade:

    def __init__(self):
        pass

    @staticmethod
    def execute_request(request: Request) -> list:
        # def pokedex vars
        api_url = "https://pokeapi.co/api/v2/"
        request_items = []
        loop = asyncio.get_event_loop()
        output_list = []
        # get mode
        if request.category == "pokemon":
            api_url += "pokemon/"
        elif request.category == "move":
            api_url += "move/"
        elif request.category == "ability":
            api_url += "ability/"

        # get data source
        if request.input_file is not None and os.path.isfile(request.input_file):
            with open(request.input_file, mode='r') as input_file:
                request_items = input_file.read().splitlines()
        else:
            request_items.append(request.input)

        results = loop.run_until_complete(process_requests(api_url, request_items))

        if request.category == "pokemon":
            print("\nconstructing pokemon object")
            # expanded expands stats, abilities, moves
            for result in results:
                if "fail" in result:
                    output_list.append(result["fail"])
                    continue
                if request.extended is False:
                    stat_list = []
                    type_list = []
                    ability_list = []
                    move_list = []
                    for stat in result["stats"]:
                        name = stat["stat"]["name"]
                        value = stat["base_stat"]
                        stat_list.append(name+": "+str(value))
                    for typename in result["types"]:
                        name = typename["type"]["name"]
                        type_list.append(name)
                    for ability in result["abilities"]:
                        name = ability["ability"]["name"]
                        ability_list.append(name)
                    for move in result["moves"]:
                        name = move["move"]["name"]
                        level = move["version_group_details"][0]["level_learned_at"]
                        move_list.append(name+" at level "+str(level))

                    output_list.append(Pokemon(result["name"], result["id"], result["height"],
                                               result["weight"], stat_list, type_list,
                                               ability_list, move_list))
                else:
                    stat_list = []
                    type_list = []
                    ability_list = []
                    move_list = []
                    for stat in result["stats"]:
                        data = loop.run_until_complete(process_single_request(stat["stat"]["url"]))
                        stat_list.append(Stats(data["name"], data["id"], stat["base_stat"], data["is_battle_only"]))
                    for typename in result["types"]:
                        name = typename["type"]["name"]
                        type_list.append(name)
                    for ability in result["abilities"]:
                        data = loop.run_until_complete(process_single_request(ability["ability"]["url"]))

                        pokemon_list = []
                        for pokemon in data["pokemon"]:
                            pokemon_list.append(pokemon["pokemon"]["name"])
                        ability_list.append(Ability(data["name"], data["id"], data["generation"]["name"],
                                                    data["effect_entries"][1]["effect"],
                                                    data["effect_entries"][1]["short_effect"],
                                                    pokemon_list))
                    for move in result["moves"]:
                        data = loop.run_until_complete(process_single_request(move["move"]["url"]))
                        move_list.append(Move(data["name"], data["id"], data["generation"]["name"],
                                              data["accuracy"], data["pp"], data["power"],
                                              data["type"]["name"], data["damage_class"]["name"],
                                              data["meta"]["ailment"]["name"]))

                    output_list.append(Pokemon(result["name"], result["id"], result["height"],
                                               result["weight"], stat_list, type_list,
                                               ability_list, move_list))
        elif request.category == "move":
            print("\nconstructing move object")
            for result in results:
                if "fail" in result:
                    output_list.append(result["fail"])
                    continue
                output_list.append(Move(result["name"], result["id"], result["generation"]["name"],
                                        result["accuracy"], result["pp"], result["power"],
                                        result["type"]["name"], result["damage_class"]["name"],
                                        result["meta"]["ailment"]["name"]))
        elif request.category == "ability":
            print("\nconstructing ability object")
            for result in results:
                if "fail" in result:
                    output_list.append(result["fail"])
                    continue
                pokemon_list = []
                for pokemon in result["pokemon"]:
                    pokemon_list.append(pokemon["pokemon"]["name"])
                output_list.append(Ability(result["name"], result["id"], result["generation"]["name"],
                                   result["effect_entries"][1]["effect"], result["effect_entries"][1]["short_effect"],
                                   pokemon_list))

        return output_list


async def get_pokedex_data(url: str, session: aiohttp.ClientSession) -> dict:
    """
    An async coroutine that executes GET http request. The response is
    converted to a json. The HTTP request and the json conversion are
    asynchronous processes that need to be awaited.
    :param url: a string, the unformatted url (missing parameters)
    :param session: a HTTP session
    :return: a dict, json representation of response.
    """
    response = await session.request(method="GET", url=url)
    if response.status == 200:
        json_dict = await response.json()
        return json_dict
    else:
        return {"fail": "\nThe request to " + url + " failed."}


async def process_single_request(url) -> dict:
    """
    This function depicts the use of await to showcase how one async
    coroutine can await another async coroutine
    :param url: a url
    :return: dict, json response
    """
    async with aiohttp.ClientSession() as session:
        response = await get_pokedex_data(url, session)
        return response


async def process_requests(url, requests: list) -> list:
    """
    This function depicts the use of asyncio.gather to run multiple
    async coroutines concurrently.
    :param requests: a list of int's
    :return: list of dict, collection of response data from the endpoint.
    """
    async with aiohttp.ClientSession() as session:
        # print("***process_requests")
        # url += id
        async_coroutines = [get_pokedex_data(url+id, session) for id in requests]
        responses = await asyncio.gather(*async_coroutines)
        return responses

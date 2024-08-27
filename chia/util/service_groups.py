from __future__ import annotations

from typing import Dict, Generator, Iterable, KeysView

SERVICES_FOR_GROUP: Dict[str, list[str]] = {
    "all": [
        "gold_harvester",
        "gold_timelord_launcher",
        "gold_timelord",
        "gold_farmer",
        "gold_full_node",
        "gold_wallet",
        "gold_data_layer",
        "gold_data_layer_http",
    ],
    "daemon": [],
    # TODO: should this be `data_layer`?
    "data": ["gold_wallet", "gold_data_layer"],
    "data_layer_http": ["gold_data_layer_http"],
    "node": ["gold_full_node"],
    "harvester": ["gold_harvester"],
    "farmer": ["gold_harvester", "gold_farmer", "gold_full_node", "gold_wallet"],
    "farmer-no-wallet": ["gold_harvester", "gold_farmer", "gold_full_node"],
    "farmer-only": ["gold_farmer"],
    "timelord": ["gold_timelord_launcher", "gold_timelord", "gold_full_node"],
    "timelord-only": ["gold_timelord"],
    "timelord-launcher-only": ["gold_timelord_launcher"],
    "wallet": ["gold_wallet"],
    "introducer": ["gold_introducer"],
    "simulator": ["gold_full_node_simulator"],
    "crawler": ["gold_crawler"],
    "seeder": ["gold_crawler", "gold_seeder"],
    "seeder-only": ["gold_seeder"],
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups: Iterable[str]) -> Generator[str, None, None]:
    for group in groups:
        yield from SERVICES_FOR_GROUP[group]


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())

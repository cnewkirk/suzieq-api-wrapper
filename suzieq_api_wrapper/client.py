"""Main SuzieQ client class."""
from ._base import _SuzieQBase
from ._address import AddressMixin
from ._arpnd import ArpndMixin
from ._bgp import BgpMixin
from ._device import DeviceMixin
from ._devconfig import DevconfigMixin
from ._evpnvni import EvpnVniMixin
from ._fs import FsMixin
from ._interface import InterfaceMixin
from ._inventory import InventoryMixin
from ._lldp import LldpMixin
from ._mac import MacMixin
from ._mlag import MlagMixin
from ._namespace import NamespaceMixin
from ._network import NetworkMixin
from ._ospf import OspfMixin
from ._path import PathMixin
from ._route import RouteMixin
from ._sqpoller import SqPollerMixin
from ._table import TablesMixin
from ._topology import TopologyMixin
from ._vlan import VlanMixin


class SuzieQ(
    _SuzieQBase,
    AddressMixin,
    ArpndMixin,
    BgpMixin,
    DeviceMixin,
    DevconfigMixin,
    EvpnVniMixin,
    FsMixin,
    InterfaceMixin,
    InventoryMixin,
    LldpMixin,
    MacMixin,
    MlagMixin,
    NamespaceMixin,
    NetworkMixin,
    OspfMixin,
    PathMixin,
    RouteMixin,
    SqPollerMixin,
    TablesMixin,
    TopologyMixin,
    VlanMixin,
):
    """Thin Python wrapper for the SuzieQ REST API (v2).

    All responses are returned as parsed Python objects (lists of dicts
    or column-oriented dicts for ``summarize``).  Failed HTTP requests
    raise :class:`~suzieq_api_wrapper.SuzieQHTTPError` (or a specific
    subclass such as :class:`~suzieq_api_wrapper.AuthenticationError`).

    Usage::

        import suzieq_api_wrapper as suzieq

        client = suzieq.SuzieQ(
            url="https://127.0.0.1:8000",
            api_key="your-api-key-here",
        )

        # Show all BGP peers
        peers = client.show_bgp()

        # Show only established peers in a specific namespace
        peers = client.show_bgp(namespace=["datacenter1"], state="Established")

        # Assert all BGP sessions pass
        results = client.assert_bgp(result="fail")

        # Longest-prefix match for an address
        match = client.lpm_route(address="10.0.0.1")

        # Find where a MAC address lives in the network
        location = client.find_network(address=["aa:bb:cc:dd:ee:ff"])

        # Show interfaces that are down
        down = client.show_interface(state="down")

    Args:
        url: Base URL of the SuzieQ REST server,
            e.g. ``"https://127.0.0.1:8000"``.
        api_key: SuzieQ API key configured as ``rest.API_KEY`` in
            ``~/.suzieq/suzieq.cfg``.  Generate one with
            ``openssl rand -hex 20``.
        verify_ssl: Whether to verify SSL certificates.  Set to ``False``
            for self-signed certs in dev/test environments (not
            recommended in production).  Defaults to ``True``.
        timeout: Socket timeout in seconds for all HTTP requests.
            Defaults to ``30``.  Pass ``None`` to disable.
        retries: Number of retries on connection errors and HTTP
            500/502/503/504 with exponential backoff (0.5 s factor).
            Defaults to ``3``.  Pass ``0`` to disable.
    """

    def __init__(self, url: str, api_key: str,
                 verify_ssl: bool = True, timeout: int = 30,
                 retries: int = 3):
        super().__init__(url, api_key, verify_ssl, timeout, retries)

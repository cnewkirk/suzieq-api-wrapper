"""Accurate SuzieQ response shapes for use in tests.

Each fixture mirrors the JSON structure returned by SuzieQ Horizon v0.20+.
``show``/``unique``/``top`` responses are lists of record dicts.
``summarize`` responses are column-oriented dicts.
"""

# ---------------------------------------------------------------------------
# address
# ---------------------------------------------------------------------------

ADDRESS_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ifname": "swp1",
        "prefix": "10.0.0.1/24",
        "ipAddressType": "ipv4",
        "ipAddress": "10.0.0.1",
        "vrf": "default",
        "type": "unicast",
        "timestamp": 1700000000000,
    }
]

ADDRESS_SUMMARIZE = {
    "count": {"all": 42},
    "ipAddressType": {"ipv4": 38, "ipv6": 4},
}

# ---------------------------------------------------------------------------
# arpnd
# ---------------------------------------------------------------------------

ARPND_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ipAddress": "10.0.0.2",
        "macaddr": "aa:bb:cc:dd:ee:ff",
        "oif": "swp1",
        "state": "reachable",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# bgp
# ---------------------------------------------------------------------------

BGP_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "peer": "10.1.0.1",
        "peerHostname": "spine01",
        "state": "Established",
        "asn": 65001,
        "peerAsn": 65000,
        "afiSafi": "ipv4Unicast",
        "numChanges": 0,
        "timestamp": 1700000000000,
    }
]

BGP_SUMMARIZE = {
    "count": {"all": 8},
    "state": {"Established": 8, "NotEstd": 0},
}

BGP_ASSERT = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "peer": "10.1.0.1",
        "assertReason": [],
        "assert": "pass",
        "timestamp": 1700000000000,
    }
]

BGP_UNIQUE = [
    {"entry": "Established", "count": 8},
    {"entry": "NotEstd", "count": 0},
]

# ---------------------------------------------------------------------------
# device
# ---------------------------------------------------------------------------

DEVICE_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "os": "cumulus",
        "vendor": "Cumulus Networks",
        "model": "VX",
        "version": "4.4.0",
        "status": "alive",
        "address": "192.168.1.1",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# interface
# ---------------------------------------------------------------------------

INTERFACE_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ifname": "swp1",
        "state": "up",
        "adminState": "up",
        "type": "ethernet",
        "mtu": 9216,
        "speed": 1000,
        "macaddr": "aa:bb:cc:dd:ee:01",
        "vrf": "default",
        "timestamp": 1700000000000,
    }
]

INTERFACE_ASSERT = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ifname": "swp1",
        "assertReason": [],
        "assert": "pass",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# route
# ---------------------------------------------------------------------------

ROUTE_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "prefix": "10.0.0.0/8",
        "nexthopIps": ["10.1.0.1"],
        "oifs": ["swp1"],
        "protocol": "bgp",
        "prefixlen": 8,
        "ipvers": 4,
        "timestamp": 1700000000000,
    }
]

ROUTE_LPM = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "prefix": "10.0.0.0/24",
        "nexthopIps": ["10.1.0.1"],
        "oifs": ["swp1"],
        "protocol": "bgp",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# network / find
# ---------------------------------------------------------------------------

NETWORK_FIND = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "ifname": "swp1",
        "ipAddress": "10.0.0.5",
        "macaddr": "aa:bb:cc:dd:ee:ff",
        "l2miss": False,
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# vlan
# ---------------------------------------------------------------------------

VLAN_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vlan": 100,
        "vlanName": "prod-vlan",
        "state": "active",
        "interfaces": ["swp1", "swp2"],
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# topology
# ---------------------------------------------------------------------------

TOPOLOGY_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ifname": "swp1",
        "peerHostname": "spine01",
        "peerIfname": "swp1",
        "via": "lldp",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# devconfig
# ---------------------------------------------------------------------------

DEVCONFIG_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "config": "interface swp1\n  description uplink\n",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# evpnVni
# ---------------------------------------------------------------------------

EVPNVNI_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vni": 10100,
        "type": "L2",
        "priVtepIp": "10.0.1.1",
        "state": "up",
        "timestamp": 1700000000000,
    }
]

EVPNVNI_ASSERT = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vni": 10100,
        "assertReason": [],
        "assert": "pass",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# fs
# ---------------------------------------------------------------------------

FS_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "mountPoint": "/",
        "usedPercent": 34,
        "used": 2048,
        "total": 6144,
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# inventory
# ---------------------------------------------------------------------------

INVENTORY_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "type": "supervisor",
        "model": "VX",
        "vendor": "Cumulus Networks",
        "serial": "SN0001",
        "status": "present",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# lldp
# ---------------------------------------------------------------------------

LLDP_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "ifname": "swp1",
        "peerHostname": "spine01",
        "peerIfname": "swp1",
        "peerMacaddr": "bb:cc:dd:ee:ff:01",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# mac
# ---------------------------------------------------------------------------

MAC_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vlan": 100,
        "macaddr": "aa:bb:cc:dd:ee:ff",
        "oif": "swp1",
        "remoteVtepIp": "",
        "flags": "dynamic",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# mlag
# ---------------------------------------------------------------------------

MLAG_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "state": "up",
        "peerAddress": "169.254.1.2",
        "peerLink": "peerlink",
        "systemId": "44:38:39:ff:01:01",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# namespace
# ---------------------------------------------------------------------------

NAMESPACE_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "os": "cumulus",
        "vendor": "Cumulus Networks",
        "model": "VX",
        "version": "4.4.0",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# ospf
# ---------------------------------------------------------------------------

OSPF_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "ifname": "swp1",
        "area": "0.0.0.0",
        "state": "full",
        "peerHostname": "spine01",
        "timestamp": 1700000000000,
    }
]

OSPF_ASSERT = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "ifname": "swp1",
        "assertReason": [],
        "assert": "pass",
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# path
# ---------------------------------------------------------------------------

PATH_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "vrf": "default",
        "ifname": "swp1",
        "nexthopIp": "10.1.0.1",
        "ipLookup": "10.0.0.5",
        "overlay": False,
        "timestamp": 1700000000000,
    }
]

# ---------------------------------------------------------------------------
# sqPoller
# ---------------------------------------------------------------------------

SQPOLLER_SHOW = [
    {
        "namespace": "datacenter1",
        "hostname": "leaf01",
        "service": "bgp",
        "status": 0,
        "pollExcdPeriodCount": 0,
        "gatherTime": 0.12,
        "totalTime": 0.15,
        "timestamp": 1700000000000,
    }
]

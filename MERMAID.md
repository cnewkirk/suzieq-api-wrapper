# Architecture Diagrams — suzieq-api-wrapper

## Package composition

`SuzieQ` (in `client.py`) is built by multiple-inheriting from `_SuzieQBase`
and one mixin class per SuzieQ table.  Dashed arrows represent mixin
inheritance; the solid arrow represents the base-class relationship.

```mermaid
flowchart TD
    caller(["Your Code"])

    subgraph routing_sg["Routing and Switching"]
        BgpMixin
        OspfMixin
        RouteMixin
        EvpnVniMixin
        VlanMixin
        MacMixin
        MlagMixin
    end

    subgraph network_sg["Network State"]
        InterfaceMixin
        AddressMixin
        ArpndMixin
        LldpMixin
        TopologyMixin
    end

    subgraph inventory_sg["Inventory and Config"]
        DeviceMixin
        DevconfigMixin
        InventoryMixin
        FsMixin
        NamespaceMixin
    end

    subgraph ops_sg["Operations"]
        PathMixin
        NetworkMixin
        SqPollerMixin
        TablesMixin
    end

    BaseClass["_SuzieQBase - _base.py<br/>_get / _parse / _build_params"]

    subgraph client_sg["client.py"]
        SuzieQ["SuzieQ<br/>flat namespace<br/>~90 public methods"]
    end

    caller -->|"client.method()"| SuzieQ

    routing_sg   -.->|"mixin"| SuzieQ
    network_sg   -.->|"mixin"| SuzieQ
    inventory_sg -.->|"mixin"| SuzieQ
    ops_sg       -.->|"mixin"| SuzieQ

    BaseClass -->|"base class"| SuzieQ

    classDef mixin  fill:#dbeafe,stroke:#3b82f6,color:#1e3a5f
    classDef core   fill:#fef3c7,stroke:#d97706,color:#78350f,font-weight:bold
    classDef base   fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef caller fill:#f1f5f9,stroke:#94a3b8,color:#334155

    class BgpMixin,OspfMixin,RouteMixin,EvpnVniMixin,VlanMixin,MacMixin,MlagMixin mixin
    class InterfaceMixin,AddressMixin,ArpndMixin,LldpMixin,TopologyMixin mixin
    class DeviceMixin,DevconfigMixin,InventoryMixin,FsMixin,NamespaceMixin mixin
    class PathMixin,NetworkMixin,SqPollerMixin,TablesMixin mixin
    class SuzieQ core
    class BaseClass base
    class caller caller
```

---

## Request lifecycle

What happens at runtime when any method on the client is called.

```mermaid
flowchart LR
    code(["your_code.py"])

    subgraph client_layer["client.py - SuzieQ"]
        method["client.show_bgp(state='Established')<br/>client.lpm_route(address='10.0.0.1')<br/>client.assert_interface(what='mtu')"]
    end

    subgraph base_layer["_base.py - _SuzieQBase"]
        direction TB
        build["_build_params(**kwargs)<br/>strips None values"]
        get["_get(table, verb, params)<br/>builds /api/v2/table/verb URL"]
        parse["_parse(response)<br/>1. raise_for_status()<br/>2. JSON -> list / dict<br/>3. empty -> None"]
        build --> get --> parse
    end

    subgraph sess_layer["requests.Session"]
        sess["API key header: access_token<br/>Accept: application/json<br/>SSL verification / connection pool<br/>urllib3 Retry (3x w/ backoff)"]
    end

    subgraph api_layer["SuzieQ REST Server"]
        v2["/api/v2/{table}/{verb}<br/>21 tables × 4-6 verbs<br/>all GET, query params only"]
    end

    result(["Python object<br/>list[dict] / dict / None"])

    code         -->|"call"| client_layer
    client_layer -->|"delegates"| build
    get          -->|"HTTP GET"| sess_layer
    sess_layer   -->|"HTTPS"| v2
    v2           -->|"JSON response"| parse
    parse        -->|"parsed value"| result

    classDef user    fill:#fff7ed,stroke:#f97316,color:#9a3412
    classDef client  fill:#fef3c7,stroke:#d97706,color:#78350f
    classDef base    fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef session fill:#eff6ff,stroke:#3b82f6,color:#1e40af
    classDef api     fill:#fdf4ff,stroke:#a855f7,color:#6b21a8

    class code,result user
    class method client
    class build,get,parse base
    class sess session
    class v2 api
```

---

## Verb availability

Which verbs are available on which tables.

```mermaid
flowchart LR
    subgraph verbs["Verbs"]
        show["show"]
        summarize["summarize"]
        unique["unique"]
        top["top"]
        assert_v["assert"]
        lpm["lpm"]
        find["find"]
    end

    subgraph all_tables["All 21 tables"]
        all["address, arpnd, bgp, device,<br/>devconfig, evpnVni, fs, interface,<br/>inventory, lldp, mac, mlag,<br/>namespace, network, ospf, path,<br/>route, sqPoller, table, topology, vlan"]
    end

    subgraph assert_tables["4 tables"]
        at["bgp, evpnVni,<br/>interface, ospf"]
    end

    subgraph route_only["route only"]
        rt["route"]
    end

    subgraph network_only["network only"]
        nt["network"]
    end

    show      --> all
    summarize --> all
    top       --> all
    unique    -->|"except devconfig"| all
    assert_v  --> at
    lpm       --> rt
    find      --> nt

    classDef verb  fill:#dbeafe,stroke:#3b82f6,color:#1e3a5f
    classDef table fill:#fef3c7,stroke:#d97706,color:#78350f

    class show,summarize,unique,top,assert_v,lpm,find verb
    class all,at,rt,nt table
```

---

*See [ARCHITECTURE.md](ARCHITECTURE.md) for the decision record behind each design choice.*

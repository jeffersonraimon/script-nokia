import string

stop = False;

while (stop == False):
    print("\n");
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=");
    print("       S C R I P T  O N T  N O K I A")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-");
    print("\n");

    try:    
        opcao = int(input("OPÇÃO: 1 - PROVISIONAR / 2 - REMOVER / 3 - SAIR: "));
        if opcao >= 1 and opcao <= 3:
            pass;
        else:
            print("INVÁLIDO! FAÇA NOVAMENTE...");
            print("\n");
            continue;
    except:
        print("\n");
        print("INVÁLIDO! FAÇA NOVAMENTE...");
        print("\n");
        continue;

    if opcao == 1:
        print("-=-=-=-=-=-=-=-= PROVISIONAR -=-=-=-=-=-=-=-=-==");
        try:
            name_client = str(input("NOME: "));
            name_client = name_client.upper()
            cx_client = str(input("CX: "));
            sn_client = str(input("S/N: "));
            sn_client = sn_client.upper();
            slot_client = int(input("SLOT: "));
            port_client = int(input("PORTA: "));
            ont_client = int(input("ONT: "));
            vlan_client = int(input("VLAN: "));
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==");
        except:
            print("\n");
            print("INVÁLIDO! FAÇA NOVAMENTE...");
            print("\n");
            continue;
        print("\n");

        print(f"""configure equipment ont interface 1/1/{slot_client}/{port_client}/{ont_client} sw-ver-pland auto desc1 "{name_client}" desc2 "CX{cx_client}" sernum ALCL:{sn_client} pland-cfgfile1 disabled optics-hist enable\nconfigure equipment ont interface 1/1/{slot_client}/{port_client}/{ont_client} admin-state up\nconfigure qos interface ont:1/1/{slot_client}/{port_client}/{ont_client} ds-queue-sharing\nconfigure equipment ont slot 1/1/{slot_client}/{port_client}/{ont_client}/14 plndnumdataports 1 plndnumvoiceports 0 planned-card-type veip admin-state up\nconfigure qos interface 1/1/{slot_client}/{port_client}/{ont_client}/14/1 upstream-queue 0 bandwidth-profile name:HSI_200M_UP\nconfigure bridge port 1/1/{slot_client}/{port_client}/{ont_client}/14/1 max-unicast-mac 10\nconfigure bridge port 1/1/{slot_client}/{port_client}/{ont_client}/14/1 vlan-id {vlan_client} tag single-tagged\nconfigure interface port uni:1/1/{slot_client}/{port_client}/{ont_client}/14/1 admin-up\nexit all""");

    if opcao == 2:
        print("\n");
        opcao2 = int(input("ONT ANTERIOR? 1 - SIM / 2 - NÃO: "));

        if opcao2 == 2:

            print("\n");
            print("-=-=-=-=-=-=-=-= REMOVER -=-=-=-=-=-=-=-=-==");
            slot_client = int(input("SLOT: "));
            port_client = int(input("PORTA: "));
            ont_client = int(input("ONT: "));
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==");

            print(f"configure equipment ont interface 1/1/{slot_client}/{port_client}/{ont_client} admin-state down\nconfigure equipment ont slot 1/1/{slot_client}/{port_client}/{ont_client} admin-state down\nconfigure interface port uni:1/1/{slot_client}/{port_client}/{ont_client}/14/1 no admin-up\nconfigure equipment ont no interface 1/1/{slot_client}/{port_client}/{ont_client}");
            continue;
        if opcao2 == 1:
            try:
                print("\n");
                print(f"configure equipment ont interface 1/1/{slot_client}/{port_client}/{ont_client} admin-state down\nconfigure equipment ont slot 1/1/{slot_client}/{port_client}/{ont_client} admin-state down\nconfigure interface port uni:1/1/{slot_client}/{port_client}/{ont_client}/14/1 no admin-up\nconfigure equipment ont no interface 1/1/{slot_client}/{port_client}/{ont_client}");
                print("\n");
            except:
                print("SEM ONT INFORMADA ANTERIORMENTE");
                print("\n");
                continue;
        else:
            print("\n");
            print("INVÁLIDO! FAÇA NOVAMENTE...");
            print("\n");
            continue;
    if opcao == 3:
        stop = True;
        break;

    print("\n");
    stopapp = int(input("PARAR? 1 - SIM / 2 - NÃO: "));

    if stopapp == 1:
        stop = True;
    
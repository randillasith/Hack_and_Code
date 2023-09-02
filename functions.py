import json  # to manipulate json files
import os  # to control the terminal window (if needed)
import xlsxwriter  # to write into Excel spreadsheet


def login():
    while True:
        name: str = input("Enter Your Name: ")
        if name != "":
            if not os.path.exists(f"./cart/{name}.txt"):
                user = open(f"./cart/{name}.txt", "w")
                user.close()
                break
            else:
                break
        else:
            continue
    return name


def addItemsToCart(part_name: str, price: float, currently_loggedIn: str):
    if currently_loggedIn != "":
        cart_file = open(f"./cart/{currently_loggedIn}.txt", "+a")
        item_format: dict = {}
        item_format[part_name] = price
        cart_file.write(f"{item_format}\n")
        cart_file.close()
        print("Item Added to cart!")
    else:
        print("You have to login first...")
        login()


def getAllData(path: str):
    with open(path) as file:
        # Load the JSON data
        parts_data = json.load(file)

    return parts_data


def cpuList(cpu_number: dict):
    cpuData = getAllData("./parts/cpu.json")
    cpu_list = cpuData["cpu"][-10:]
    n: int = 1
    for cpu in cpu_list:
        print(f"\t{n}. {cpu['brand']} {cpu['model']}")
        cpu_number[n] = cpu["model"]
        n += 1


def getCpuData(index: int, cpu_number: dict):
    cpu_name = cpu_number.get(index)
    cpuData = getAllData("./parts/cpu.json")
    cpu_list = cpuData["cpu"][-10:]
    data = cpu_list[index - 1]
    try:
        if data["boost_clock"]["cycles"] != None:
            boostClock = round((data["boost_clock"]["cycles"]) / 1000**3, 2)
            boostClock = str(boostClock) + "GHz"
        else:
            boostClock = None
    except TypeError:
        if data["boost_clock"] != None:
            boostClock = round((data["boost_clock"]) / 1000**3, 2)
            boostClock = str(boostClock) + "GHz"
        else:
            boostClock = None
    print(
        f"""
    Details of {cpu_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Base Clock - {round((data['base_clock']['cycles']) / 1000 ** 3, 2)}GHz
          Boost Clock - {boostClock}
          Integrated Graphics - {data['integrated_graphics']}
          TDP - {data['tdp']}W
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def ramList(ram_number: dict):
    ramData = getAllData("./parts/ram.json")
    ram_list = ramData["memory"][-10:]
    n: int = 1
    for ram in ram_list:
        print(f"\t{n}. {ram['brand']} {ram['model']}")
        ram_number[n] = ram["model"]
        n += 1


def getRamData(index: int, ram_number: dict):
    ram_name = ram_number.get(index)
    ramData = getAllData("./parts/ram.json")
    ram_list = ramData["memory"][-10:]
    data = ram_list[index - 1]
    try:
        if data["speed"]["cycles"] != None:
            speed = round((data["speed"]["cycles"]) / 1000**3, 2)
            speed = str(speed) + "GHz"
        else:
            speed = None
    except TypeError as e:
        print(e)

    print(
        f"""
    Details of {ram_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Module Type - {data['module_type']}
          Speed - {speed}
          No. of Modules - {data['number_of_modules']}
          Module Size - {round((data['module_size']) / 1024 ** 3, 2)}GB
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def hddList(hdd_number: dict):
    hddData = getAllData("./parts/hdd.json")
    hdd_list = hddData["hdd"][-10:]
    n: int = 1
    for hdd in hdd_list:
        print(f"\t{n}. {hdd['brand']} {hdd['model']}")
        hdd_number[n] = hdd["brand"] + " " + hdd["model"]
        n += 1


def getHddData(index: int, hdd_number: dict):
    hdd_name = hdd_number.get(index)
    hddData = getAllData("./parts/hdd.json")
    hdd_list = hddData["hdd"][-10:]
    data = hdd_list[index - 1]
    try:
        if data["capacity"] != None:
            capacity = round((data["capacity"]) / 1000**3, 2)
            capacity = str(capacity) + "GB"
        else:
            capacity = None
    except TypeError as e:
        print(e)

    print(
        f"""
    Details of {hdd_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Type - {data['storage_type']}
          Interface - {data['interface']}
          Form factor - {data['form_factor']}
          Capacity - {capacity}
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def mbList(mb_number: dict):
    mbData = getAllData("./parts/motherboards.json")
    mb_list = mbData["motherboard"][-10:]
    n: int = 1
    for mb in mb_list:
        print(f"\t{n}. {mb['brand']} {mb['model']}")
        mb_number[n] = mb["brand"] + " " + mb["model"]
        n += 1


def getMbData(index: int, mb_number: dict):
    mb_name = mb_number.get(index)
    mbData = getAllData("./parts/motherboards.json")
    mb_list = mbData["motherboard"][-10:]
    data = mb_list[index - 1]
    try:
        if data["max_ram"] != None:
            max_ram = round((data["max_ram"]) / 1000**3, 2)
            max_ram = str(max_ram) + "GB"
        else:
            max_ram = None
    except TypeError as e:
        print(e)

    print(
        f"""
    Details of {mb_name}
          Brand - {data['brand']}
          Model - {data['model']}
          CPU Soket - {data['soket']}
          Form factor - {data['form_factor']}
          RAM Slots - {data['ram_slots']}
          Maximum RAM - {max_ram}
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def psuList(psu_number: dict):
    psuData = getAllData("./parts/psu.json")
    psu_list = psuData["psu"][-10:]
    n: int = 1
    for psu in psu_list:
        print(f"\t{n}. {psu['brand']} {psu['model']}")
        psu_number[n] = psu["brand"] + " " + psu["model"]
        n += 1


def getPsuData(index: int, psu_number: dict):
    psu_name = psu_number.get(index)
    psuData = getAllData("./parts/psu.json")
    psu_list = psuData["psu"][-10:]
    data = psu_list[index - 1]

    print(
        f"""
    Details of {psu_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Form factor - {data['form_factor']}
          Efficiency Rating - {data['efficiency_rating']}
          Wattage - {data['wattage']}W
          Modular - {data['modular']}
          Colour - {data['color']}
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def casingList(case_number: dict):
    caseData = getAllData("./parts/casing.json")
    case_list = caseData["case"][-10:]
    n: int = 1
    for psu in case_list:
        print(f"\t{n}. {psu['brand']} {psu['model']}")
        case_number[n] = psu["brand"] + " " + psu["model"]
        n += 1


def getCasingData(index: int, case_number: dict):
    psu_name = case_number.get(index)
    caseData = getAllData("./parts/casing.json")
    case_list = caseData["case"][-10:]
    data = case_list[index - 1]

    print(
        f"""
    Details of {psu_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Form factor - {data['form_factor']}
          Colour - {data['color']}
          External Bays - {data['external_bays']}
          Internal Bays - {data['internal_bays']}
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def scrnList(scren_number: dict):
    scrnData = getAllData("./parts/monitor.json")
    scrn_list = scrnData["Monitor"][-10:]
    n: int = 1
    for psu in scrn_list:
        print(f"\t{n}. {psu['brand']} {psu['model']}")
        scren_number[n] = psu["brand"] + " " + psu["model"]
        n += 1


def getScrnData(index: int, scren_number: dict):
    scrn_name = scren_number.get(index)
    scrnData = getAllData("./parts/monitor.json")
    scrn_list = scrnData["Monitor"][-10:]
    data = scrn_list[index - 1]

    print(
        f"""
    Details of {scrn_name}
          Brand - {data['brand']}
          Model - {data['model']}
          Size - {data['size']}
          Resolution - {data['resolution']['width']}x{data['resolution']['height']}
          Refresh Rate - {data['refresh_rate']}
          Aspect Ratio - {data['aspect_ratio']}
          Price - {data['price']['amount']}{data['price']['currency']}"""
    )
    return [data["brand"] + " " + data["model"], data["price"]["amount"]]


def deleteItems():
    pass


def writeToExcel():
    pass

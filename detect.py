def read_file(li, name):
    f = open("userdict/" + name, 'rt', encoding='utf-8')
    while True:
        line = f.readline()
        if not line:
            break
        li.append(line.strip())
    f.close()


human = []
read_file(human, 'person/criminal')
read_file(human, 'person/famous')
read_file(human, 'person/politician')
organization = []
read_file(organization, 'org/company')
read_file(organization, 'org/gov')
read_file(organization, 'org/party')
position = []
read_file(position, 'position')


def is_human(str):
    return str in human


def is_org(str):
    return str in organization


def is_pos(str):
    return str in position

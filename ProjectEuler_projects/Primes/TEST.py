
def update_array(file, m_array):
    with open(file) as f:
        var = f.readlines()

    var = str(var)
    for character in "[], '": # replaces each of: ',[] and whitespace with nothing
        var = var.replace(character, '')

    local_array = []
    for x in var:
        local_array.append(int(x))

    m_array = local_array.copy()



m = []
print(m)
update_array("prime_array.txt", m)
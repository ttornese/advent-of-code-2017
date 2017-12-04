def read_data_from_file(fileName):
    dataFile = open(fileName, "r")
    passphrases = []

    for line in dataFile:
        passphrases.append(line)

    return passphrases

def validate_part_one(phrases):
    phrasesSeen = {}
    for phrase in phrases:
        if phrase in phrasesSeen:
            return False
        else:
            phrasesSeen[phrase] = True

    return True


def validate_part_two(phrases):
    for i in range(0, len(phrases)):
        for j in range(i + 1, len(phrases)):
            if sorted(list(phrases[i])) == sorted(list(phrases[j])):
                return False

    return True

def validate_passphrase(passphrase, part):
    phrases = passphrase.split()
    if part == 'partOne':
        return validate_part_one(phrases)
    else:
        return validate_part_two(phrases)

def find_total_valid_passphrases(passphrases, part):
    count = 0
    for passphrase in passphrases:
        if validate_passphrase(passphrase, part):
            count += 1

    return count

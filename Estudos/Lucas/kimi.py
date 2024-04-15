import sys


def toMillis(time: str) -> int:
    timeSplit = time.split(":")
    timeMillis = 0
    timeMillis += int(timeSplit[0]) * 1000 * 60
    timeMillis += int(timeSplit[1]) * 1000
    timeMillis += int(timeSplit[2])
    return timeMillis


def getRacerLaps(racerInputs: list[str], numberOfLaps: int):
    racerLaps: list[int] = []
    for lap in range(numberOfLaps):
        racerLaps.append(toMillis(racerInputs[1 + lap]))
    return racerLaps


def getRanking(racerInfos: list[list[int]]) -> list[int]:
    rankedRacerInfos = racerInfos.copy()
    rankedRacerInfos.sort(key=lambda _racerInfo: _racerInfo[1])
    ranking = []
    for racerInfo in rankedRacerInfos:
        ranking.append(racerInfo[0])
    return ranking


def main(firstInputsStr: str, racerInputsStr: list[str]):
    # initialInputs = input().split(" ") TODO Replace commented line with below when ready
    numberOfRacers, numberOfLaps = map(int, firstInputsStr.split())

    bestLap = sys.maxsize
    racerWithBestLap = -1

    racersInfos: list[list[int]] = []

    for _ in range(numberOfRacers):
        # racerInputs: list[str] = input().split(" ") TODO Replace commented line with below when ready
        racerInputs: list[str] = racerInputsStr[_].split()

        racerNumber: int = int(racerInputs[0])
        racerLaps = getRacerLaps(racerInputs, numberOfLaps)
        racerFullTime = sum(racerLaps)

        racersInfos.append([racerNumber, racerFullTime] + racerLaps)

    ranking = getRanking(racersInfos)

    for racerInfo in racersInfos:
        racerNumber = racerInfo[0]
        racerLaps = racerInfo[2:2 + numberOfLaps]
        bestRacerLap = min(racerLaps)
        if bestRacerLap == bestLap:
            if ranking.index(racerWithBestLap) >= 10:
                racerWithBestLap = racerNumber
        if bestRacerLap < bestLap:
            bestLap = bestRacerLap
            racerWithBestLap = racerNumber

    if ranking.index(racerWithBestLap) < 10:
        print(racerWithBestLap)
    else:
        print("NENHUM")


if __name__ == '__main__':
    main("12 2",
         [
             "55 1:44:581 1:44:893",
             "1 1:50:881 1:44:198",
             "11 1:45:981 1:45:091",
             "16 1:44:861 1:44:201",
             "8 1:46:203 1:44:199",
             "10 1:46:027 1:44:199",
             "44 1:47:212 1:46:128",
             "63 1:46:891 1:45:980",
             "23 1:48:373 1:47:082",
             "4 1:47:570 1:46:096",
             "3 1:47:298 1:45:976",
             "5 1:48:584 1:46:493"
         ])

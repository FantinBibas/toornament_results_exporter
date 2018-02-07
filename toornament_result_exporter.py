#!/usr/bin/env python3

import requests
import json

def getBasicParticipantInfo(participant):
    participantInfos = participant['participant']['id'] + ','
    participantInfos += participant['participant']['name'] + ','
    participantInfos += str(participant['result']) + ','
    participantInfos += str(participant['score']) + ','
    return participantInfos

def printBasicMatchesInfo(loadedJson):
    print('participantAId,participantAName,particpantAResult,participantAScore,participantBId,participantBName,particpantBResult,participantBScore,')
    for match in loadedJson:
        participantA = getBasicParticipantInfo(match['opponents'][0])
        participantB = getBasicParticipantInfo(match['opponents'][1])
        print(participantA + participantB)

def main():
    apikey = input('Enter your API Key: ')
    toornamenentId = input('Enter the toornament ID: ')
    headers = {'X-Api-Key': apikey}
    url = 'https://api.toornament.com/v1/tournaments/' + toornamenentId + '/matches'
    rawJson = requests.get(url, headers=headers).text
    loadedJson = json.loads(rawJson)
    printBasicMatchesInfo(loadedJson)

if __name__ == '__main__':
    main()

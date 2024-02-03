#!/usr/bin/node

//Using the test expression
const sentence_1 = 'The dog chased the cat'
const regex_1 = /the/
console.log("Matching literals 1: " + regex_1.test(sentence_1))

const sentence_2 = 'Hello World!'
const regex_2 = /Hello/
console.log("Matching literals 1: " + regex_2.test(sentence_2))

//Matching string literals
const waldoIsHiding = "Somewhere Waldo is hiding"
const waldoRegex = /Waldo/
console.log("Exact literals: " + waldoRegex.test(waldoIsHiding))

//Matching multiple string literals
const nachbarnTiere = "unser Nachbar hat einen Hund"
const hausTiere = /Katze|Ente|Hund/
console.log("Testing multiple: " + hausTiere.test(nachbarnTiere))

//Ignoring case
const mySchool = "FreeCodeCamp"
const myStudy = /freecodecamp/i
console.log("Ignore case: " + mySchool.match(myStudy))

//Multiple matches
const aSong = "Twinkle twinkle twinky"
const aWord = /twink/ig
console.log("Multiple matches: " + aSong.match(aWord))

//in js a period is a wildcard that stands for any one charcater
const firstSong = "I'll hum another song"
const secondSong = "Then I'll hug a bear"
const bWord = /hu./
console.log("Wildlings play wildcards: " + firstSong.match(bWord))
console.log("Free Folk play wildcards: " + secondSong.match(bWord))

//Matching multiple singular characters
const multipleChar = /[aeiou]/ig
console.log("Multiple Single Characters: " + firstSong.match(multipleChar))

//Match a range of characters
const alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
console.log("only aA to lL: " + alphabet.match(/[a-z]/ig))

//Matching different typed ranges
const quoteSample = "Blueberry 3.1415926537s are awesome"
console.log("Matching diverse range types: " + quoteSample.match(/[1-5h-s]/ig))

//Negating charcaters while matching
const schmutzig = "3 blind mice"
console.log("Not match no.s and vowels: " + schmutzig.match(/[^0-9aeiou]/ig))

//Matching characters that occur one or more times
const groSWort = "Mississipsi"
console.log("Match 1 or more 's': " + groSWort.match(/s+/ig))

//Matching characters that occur zero or more times
const soccerWort = "goooooaal"
const gPhrase = "Got me a gut feeling General Ghao"
const oPhrase = "over the moon"
console.log("In soccerWort: " + soccerWort.match(/go*/ig))
console.log("In gPhrase: " + gPhrase.match(/go*/ig))
console.log("In oPhrase: " + oPhrase.match(/go*/ig))


/*
 * Greedy and lazy matches
 * Greedy match: matches the longest occurrence of said phrase
 * Lazy match: matches the shortest occurrence of said phrase
 */
const recWord = "titanic"
const rec2Word = "taiwanit"
const gMatch = /t[a-z]*i/
/*
 * This would match the longest phrase
 * 	then any other characters then end with an i
 * 	hence 'titani' and 'taiwani'
 */
const lMatch = /t[a-z]*?i/
/*
 * This would match the shortest phrase
 * 	then any 0 and/or the least possible characters then end with an i
 * 	hence 'ti' and 'tai'
 */
console.log("Greedy titanic: " + recWord.match(gMatch))
console.log("Greedy taiwanit: " + rec2Word.match(gMatch))
console.log("Lazy titanic: " + recWord.match(lMatch))
console.log("Lazy taiwanit: " + rec2Word.match(lMatch))

const theNorth = "<h1>Winter is coming<h1>"
console.log("Crazy Match: " + theNorth.match(/<.*>/))

//Criminals escaped and like to stay together in crowds, find em
//Criminals are 'C'
const crowd = "P1P2P3P4P5P6CCCCP7P8P9"
console.log("Bumass criminals: " + crowd.match(/C+/))

//Match only if it starts
const RickyCal = "Ricky and Cal like racing"
const CalRicky = "Cal and Ricky like racing"
console.log("Match RickyCal: " + /^Cal/.test(RickyCal))
console.log("Match CalRicky: " + /^Cal/.test(CalRicky))

//Match only if it ends
const RaceEnd = "Ricky and Cal like racing"
const RaceMid = "Cal and Ricky racing gern"
console.log("Match RickyCal: " + /racing$/.test(RaceEnd))
console.log("Match CalRicky: " + /racing$/.test(RaceMid))

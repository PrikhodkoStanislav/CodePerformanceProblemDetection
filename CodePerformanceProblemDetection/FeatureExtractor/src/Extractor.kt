import java.io.BufferedReader
import java.io.File

fun main(args: Array<String>) {
    val file = "test.kt"

    val bufferedReader: BufferedReader = File(file).bufferedReader()

    val lineList = mutableListOf<String>()

    bufferedReader.useLines { lines -> lines.forEach { lineList.add(it) } }

//    val inputString = bufferedReader.use { it.readText() }
//    println(inputString)

//    val length = inputString.length

    var numSpaces = 0
    var numTabs = 0
    var numNewLines = 0
    var numEmptyLines = 0
    var numTabsLeadLines = 0

    var length = 0

//    for (i in inputString) {
//        when(i) {
//            ' ' -> numSpaces++
//            '\t' -> numTabs++
//            '\n' -> numNewLines++
//        }
//    }

    for (line in lineList) {
        line.forEach {
            when (it) {
                ' ' -> numSpaces++
                '\t' -> numTabs++
            }
        }

        numNewLines++

        // itLingth without new-line symbol
        val itLength = line.length
        length += itLength

        if (itLength > 0) {
            when (line[0]) {
                ' ' -> numTabsLeadLines++
                '\t' -> numTabsLeadLines++
            }
        }
        if (itLength == 0)
            numEmptyLines++
    }

    val whiteSpaceRatio = numSpaces + numTabs + numNewLines

//    println(numSpaces)
//    println(numTabs)
//    println(numNewLines)
//    println(numEmptyLines)
//    println(numTabsLeadLines)
//    println(whiteSpaceRatio)
//    println(length + numNewLines - whiteSpaceRatio)

    val featureNumTabs = if (numTabs == 0) 0.0 else Math.log(numTabs.toDouble() / length)
    val featureNumSpaces = if (numSpaces == 0) 0.0 else Math.log(numSpaces.toDouble() / length)
    val featureNumEmptyLines = if (numEmptyLines == 0) 0.0 else Math.log(numEmptyLines.toDouble() / length)
    val featureWhiteSpaceRatio = whiteSpaceRatio.toDouble() / (length + numNewLines - whiteSpaceRatio)
    val featureNumTabsLeadLines = if (numTabsLeadLines * 2 >= numNewLines) 1 else 0

    println(featureNumTabs)
    println(featureNumSpaces)
    println(featureNumEmptyLines)
    println(featureWhiteSpaceRatio)
    println(featureNumTabsLeadLines)
}
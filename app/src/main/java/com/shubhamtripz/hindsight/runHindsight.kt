package com.shubhamtripz.hindsight

import com.chaquo.python.PyObject
import com.chaquo.python.Python

fun runHindsight(inputPath: String, outputName: String, format: String) {
    val python = Python.getInstance()
    val hindsightScript = python.getModule("hindsight")  // Adjust if necessary

    // Prepare arguments
    val args = listOf(
        "-i", inputPath,
        "-o", outputName,
        "-f", format
    )

    // Call the main function of the script with the prepared arguments
    hindsightScript.callAttr("main", *args.toTypedArray())
}

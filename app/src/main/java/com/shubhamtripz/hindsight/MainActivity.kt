package com.shubhamtripz.hindsight

import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Example: Run the Hindsight script
        runHindsight("/storage/emulated/0/Chrome/User Data/Default", "hindsight_output", "xlsx")
    }
}
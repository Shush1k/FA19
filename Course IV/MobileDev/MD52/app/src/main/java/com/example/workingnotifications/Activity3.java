package com.example.workingnotifications;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

public class Activity3 extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_activity3);
        setContentView(R.layout.activity_activity2);
        TextView textView = findViewById(R.id.textView);
        textView.setText("Activity3");
    }
}
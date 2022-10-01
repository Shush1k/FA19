package com.example.md51;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    boolean flag = false;
    ServiceConnection serviceConnection;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        serviceConnection = new ServiceConnection() {
            public void onServiceConnected(ComponentName name, IBinder binder) {
                flag = true;
            }
            public void onServiceDisconnected(ComponentName name) {
                flag = false;
            }
        };
    }


    public void Start(View view) {
        startService(new Intent(this, MyService.class));
    }

    public void Bind(View view) {
        bindService(new Intent(this, MyService.class), serviceConnection, BIND_AUTO_CREATE);
    }
}
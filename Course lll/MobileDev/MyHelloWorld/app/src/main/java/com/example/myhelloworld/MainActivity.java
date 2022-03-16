package com.example.myhelloworld;

import android.os.Bundle;

import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.view.View;

import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.example.myhelloworld.databinding.ActivityMainBinding;

import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);


    }

    public void onButtonClick (View view){
        EditText el1 = (EditText)findViewById(R.id.num1);
        EditText el2 = (EditText)findViewById(R.id.num2);
        TextView res = (TextView)findViewById(R.id.res);

        double num1 = Integer.parseInt(el1.getText().toString());
        double num2 = Integer.parseInt(el2.getText().toString());
        double result = num1 + num2;
        res.setText(Double.toString(result));
    }
}
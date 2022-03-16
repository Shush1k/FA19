package com.example.task1_4;
import static com.example.task1_4.R.id.*;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.*;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements View.OnClickListener, AdapterView.OnItemClickListener {

    TextView mainTextView;
    Button mainButton, okBtn, cncBtn;
    EditText mainEditText;
    ListView mainListView;
    ArrayAdapter<String> mArrayAdapter;
    ArrayList<String> mNameList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mainTextView = findViewById(main_textview);
        mainButton = findViewById(main_button);
        mainEditText = findViewById(main_edittext);
        mainListView = findViewById(main_listview);
        okBtn = findViewById(ok_btn);
        cncBtn = findViewById(cnc_btn);

        View.OnClickListener oclBtnListener = this::oclBtnClicked;

        mainButton.setOnClickListener(this);
        okBtn.setOnClickListener(oclBtnListener);
        cncBtn.setOnClickListener(oclBtnListener);

        mArrayAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, mNameList);
        mainListView.setAdapter(mArrayAdapter);
        mainListView.setOnItemClickListener(this);

    }

    @Override
    public void onClick(View v) {
        String newItemStr = mainEditText.getText().toString();

        if (newItemStr.equals("")) {
            Toast.makeText(getApplicationContext(), "Пустой элемент", Toast.LENGTH_LONG).show();
            return;
        }

        for (String item : mNameList) {
            if (item.equals(newItemStr)) {
                String errorStr = String.format("Повторный ввод элемента %s", newItemStr);
                Toast.makeText(getApplicationContext(), errorStr, Toast.LENGTH_LONG).show();
                return;
            }
        }

        mNameList.add(newItemStr);
        mArrayAdapter.notifyDataSetChanged();
    }


    @Override
    public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
        Log.d("KEKW", "item" + position + ": " + mNameList.get(position));
        mainTextView.setText(mNameList.get(position));

    }

    private void oclBtnClicked(View v) {

        switch (v.getId()) {
            case ok_btn:
                Toast.makeText(getApplicationContext(), "Кнопка ОК", Toast.LENGTH_LONG).show();
                break;
            case cnc_btn:
                Toast.makeText(getApplicationContext(), "Кнопка Cancel", Toast.LENGTH_LONG).show();
                break;
        }

    }
}
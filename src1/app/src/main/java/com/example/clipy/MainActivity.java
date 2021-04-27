package com.example.clipy;

import androidx.appcompat.app.AppCompatActivity;
import android.widget.Button;
import android.widget.EditText;
import android.view.View;
import android.os.Bundle;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class MainActivity extends AppCompatActivity {
//    Button button;
//    DatabaseReference ref;

//    private Button button;
    DatabaseReference ref;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

//        button = findViewById(R.id.button3);
//
//        button.setOnClickListener(new View.OnClickListener(){
//            @Override
//            public void onClick(View v){
//                ref.setValue("sommething");
//            }
//        });
        ref = FirebaseDatabase.getInstance().getReference().child("/Data/");
        ref.setValue("Hello!!!");

    }
}
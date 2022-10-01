package com.example.workingnotifications;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.app.Service;
import android.content.Intent;
import android.os.Build;
import android.os.IBinder;
import android.util.Log;

import androidx.core.app.NotificationCompat;

public class MyService extends Service {
    NotificationManager notifManger;
    private String TAG = "Life cycle";
    private static final int NOTIFICATION_ID=1;
    private static final String CHANNEL_ID = "CHANNEL_ID";
    @Override
    public void onCreate() {
        super.onCreate();
        Log.i(TAG, "onCreate()");
        notifManger = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        Notification notification = createForegroundNotification();
        startForeground(NOTIFICATION_ID, notification);
        //notifManger.notify(NOTIFICATION_ID,notification);


    }
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        Log.i(TAG, "onStartCommand()");

        return super.onStartCommand(intent, flags, startId);
    }
    private Notification createForegroundNotification() {
        createNotificationChannel(notifManger);
        Intent resultIntent2 = new Intent(this, Activity2.class);
        PendingIntent resultPendingIntent2 = PendingIntent.getActivity(this, 0, resultIntent2, 0);

        Intent resultIntent3 = new Intent(this, Activity3.class);
        PendingIntent resultPendingIntent3 = PendingIntent.getActivity(this, 0, resultIntent3, 0);

        Notification notification = new NotificationCompat.Builder(this, CHANNEL_ID)
                .setSmallIcon(R.mipmap.ic_launcher_round)
                .setWhen(System.currentTimeMillis())
                .setContentTitle("App")
                .setContentText("Notification")
                .setContentIntent(resultPendingIntent2)
                .addAction(R.mipmap.ic_launcher, "Activity2", resultPendingIntent2)
                .addAction(R.mipmap.ic_launcher, "Activity3", resultPendingIntent3)
                .build();
        return notification;

    }
    private void createNotificationChannel(NotificationManager manager){
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            NotificationChannel notificationChannel = new NotificationChannel(CHANNEL_ID, CHANNEL_ID, NotificationManager.IMPORTANCE_HIGH);
            manager.createNotificationChannel(notificationChannel);
        }
    }
        @Override
    public IBinder onBind(Intent intent) {
        return null;
//        throw new UnsupportedOperationException("Not yet implemented");
    }
}
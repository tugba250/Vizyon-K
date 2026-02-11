using System;
using System.Io;
using System.windows.Form;

public partial class Dashboard : Form{
    private void onTimerTick(object sender,EventArgs e){
        string path = "alerts.log";
        if (File.Exists(path)){
            string[] logs = File.ReadAllLines(path);
            if(logs.Length > 0){
                [cite_start]//en son tespiti kullanıcıya gösterir
                string lastDetection = logs[logs.Length-1];
                lblStatus.Text = "WARNING:"+ lastDetection;
                System.Media.SystemSounds.Beep.Play();
            }
        }



            }
        }
    

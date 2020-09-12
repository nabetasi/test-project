package com.example.myapplication

import android.media.MediaMetadataRetriever
import android.os.Bundle
import com.google.android.material.snackbar.Snackbar
import androidx.appcompat.app.AppCompatActivity
import android.view.Menu
import android.view.MenuItem
import android.os.AsyncTask
import com.jcraft.jsch.ChannelExec
import com.jcraft.jsch.JSch
import java.io.ByteArrayOutputStream
import java.util.*

import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*
import java.lang.Exception

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //SshTask().execute()

        //val textView = findViewById<TextView>(R.id.myLabel)

        //val button = findViewById<Button>(R.id.button2)

        button2.setOnClickListener {
            val username = userName.text.toString()
            val hostname = hostName.text.toString()
            usernameText.text = username
            hostnameText.text = hostname
            SshTask().execute(username, hostname)
            //val output = executeRemoteCommand( username, "wssrk0hk", hostname)
            //myLabel.text = output
        }


        setSupportActionBar(toolbar)

        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                .setAction("Action", null).show()
        }


    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }

    class SshTask : AsyncTask<String, Void, String>() {
        override fun doInBackground(vararg params: String): String {
            val output = executeRemoteCommand(params[0], "wssrk0hk", params[1])
            print(output)
            return output
        }
    }
}

fun executeRemoteCommand(username: String,
                         password: String,
                         hostname: String,
                         port: Int = 22): String {
    val jsch = JSch()
    try {
        val session = jsch.getSession(username, hostname, port)
        session.setPassword(password)

        //Avoid asking for key confirmation
        val properties = Properties()
        properties.put("StrictHostKeyChecking", "no")
        session.setConfig(properties)

        session.connect()

        //Create SSH Channel
        val sshChannel = session.openChannel("exec") as ChannelExec
        val outputStream = ByteArrayOutputStream()
        sshChannel.outputStream = outputStream

        //Execute command
        sshChannel.setCommand("ls -al")
        sshChannel.connect()

        //Sleep needed in order to wait long enough to get result back
        Thread.sleep(1_000)
        sshChannel.disconnect()

        session.disconnect()

        return outputStream.toString()
    } catch (e: Exception) {
        print(e)
        return "fail"
    }
}

fun executeHotSpotCommand(username: String,
                         password: String,
                         hostname: String,
                         port: Int = 22): Boolean {
    val jsch = JSch()
    try {
        val session = jsch.getSession(username, hostname, port)
        session.setPassword(password)

        //Avoid asking for key confirmation
        val properties = Properties()
        properties.put("StrictHostKeyChecking", "no")
        session.setConfig(properties)

        session.connect()

        //Create SSH Channel
        val sshChannel = session.openChannel("exec") as ChannelExec
        val outputStream = ByteArrayOutputStream()
        sshChannel.outputStream = outputStream

        //Execute command
        sshChannel.setCommand("ls -al")
        sshChannel.connect()

        //Sleep needed in order to wait long enough to get result back
        Thread.sleep(1_000)
        sshChannel.disconnect()

        session.disconnect()
        return true
    } catch (e:Exception) {
        print(e)
        return false
    }

}

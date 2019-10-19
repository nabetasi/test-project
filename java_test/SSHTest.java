import com.jcraft.jsch.ChannelExec;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.JSchException;
import com.jcraft.jsch.Session;
import com.jcraft.jsch.SftpException;
import java.io.BufferedInputStream;
import java.io.ByteArrayOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
 
/**
 *
 * @author tool-taro.com
 */
public class SSHTest {
 
    public static void main(String[] args) throws JSchException, SftpException, UnsupportedEncodingException, FileNotFoundException, IOException {
 
        //サーバ
        String host = "ホスト名";
        //ポート
        int port = 22;
        //ユーザ
        String user = "ユーザ";
        //パスワード
        String password = "パスワード";
        //コマンド
        String command = "date";
 
        JSch jsch;
        Session session = null;
        ChannelExec channel = null;
        BufferedInputStream bin = null;
 
        try {
            //接続
            jsch = new JSch();
            session = jsch.getSession(user, host, port);
            //known_hostsのチェックをスキップ
            session.setConfig("StrictHostKeyChecking", "no");
            session.setPassword(password);
            session.connect();
 
            channel = (ChannelExec) session.openChannel("exec");
            channel.setCommand(command);
            channel.connect();
 
            //コマンド実行
            bin = new BufferedInputStream(channel.getInputStream());
            ByteArrayOutputStream bout = new ByteArrayOutputStream();
            byte[] buf = new byte[1024];
            int length;
            while (true) {
                length = bin.read(buf);
                if (length == -1) {
                    break;
                }
                bout.write(buf, 0, length);
            }
            //標準出力
            System.out.format("実行結果=%1$s", new String(bout.toByteArray(), "UTF-8"));
        }
        finally {
            if (bin != null) {
                try {
                    bin.close();
                }
                catch (Exception e) {
                }
            }
            if (channel != null) {
                try {
                    channel.disconnect();
                }
                catch (Exception e) {
                }
            }
            if (session != null) {
                try {
                    session.disconnect();
                }
                catch (Exception e) {
                }
            }
        }
    }
}
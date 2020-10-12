import java.sql.*;

class MySql {

    public static void main (String[] args) {
        try {

            String url = "jdbc:mysql://3.8.24.94:3306/";
            String db = "db_emp_db";
            String driver = "com.mysql.jdbc.Driver";
            String user = "root";
            String pass = "Passw0rd!23";
            Class.forName(driver).newInstance();

            Connection conn = DriverManager.getConnection(url+db,user,pass);

            Statement stmt = conn.createStatement();
            ResultSet rs;

            rs = stmt.executeQuery("SELECT * FROM  tbl_emp_db");
            System.out.println("EmpID: " + "\t" + "FirstName: "+ "\t" + "LastName: "+ "\t" + "Location: ");
            /*
            while ( rs.next() ) {
                String lastName = rs.getString("Lname");
                System.out.println(lastName);
            }
            */
            conn.close();

        } catch (Exception e) {
            System.err.println("Got an exception! ");
            System.err.println(e.getMessage());
        }

    }

}

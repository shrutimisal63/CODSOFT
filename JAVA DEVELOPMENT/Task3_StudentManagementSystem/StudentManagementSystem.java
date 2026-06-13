import java.awt.*;
import java.io.*;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class StudentManagementSystem extends JFrame {

    JTextField txtName, txtId, txtGrade, txtDob;
    JTextField txtContact, txtEmail, txtSearch;

    JRadioButton maleBtn, femaleBtn;

    JButton addBtn, deleteBtn, resetBtn, searchBtn;

    JTable table;
    DefaultTableModel model;

    public StudentManagementSystem() {

        setTitle("Student Management System");
        setSize(850, 550);
        setLayout(null);

        JLabel title = new JLabel("STUDENT MANAGEMENT SYSTEM");
        title.setFont(new Font("Arial", Font.BOLD, 28));
        title.setBounds(180, 20, 500, 40);
        add(title);

        addLabel("Student Name", 40, 100);
        addLabel("Student ID", 40, 135);
        addLabel("Student Grade", 40, 170);
        addLabel("Date Of Birth", 40, 205);
        addLabel("Gender", 40, 240);
        addLabel("Contact No", 40, 275);
        addLabel("Email", 40, 310);

        txtName = createField(170, 100);
        txtId = createField(170, 135);
        txtGrade = createField(170, 170);
        txtDob = createField(170, 205);
        txtContact = createField(170, 275);
        txtEmail = createField(170, 310);

        maleBtn = new JRadioButton("Male");
        femaleBtn = new JRadioButton("Female");

        maleBtn.setBounds(170, 240, 80, 25);
        femaleBtn.setBounds(250, 240, 80, 25);

        ButtonGroup bg = new ButtonGroup();
        bg.add(maleBtn);
        bg.add(femaleBtn);

        add(maleBtn);
        add(femaleBtn);

        addBtn = new JButton("Add Student");
        resetBtn = new JButton("Reset");
        deleteBtn = new JButton("Delete");

        addBtn.setBounds(550, 130, 150, 30);
        resetBtn.setBounds(550, 175, 150, 30);
        deleteBtn.setBounds(550, 220, 150, 30);

        add(addBtn);
        add(resetBtn);
        add(deleteBtn);

        txtSearch = new JTextField();
        txtSearch.setBounds(40, 360, 250, 25);
        add(txtSearch);

        searchBtn = new JButton("Search By ID");
        searchBtn.setBounds(300, 360, 130, 25);
        add(searchBtn);

        String[] cols = {
                "Name","ID","Grade","DOB",
                "Gender","Contact","Email"
        };

        model = new DefaultTableModel(cols,0);

        table = new JTable(model);

        JScrollPane sp = new JScrollPane(table);
        sp.setBounds(40,400,760,100);
        add(sp);

        loadData();

        addBtn.addActionListener(e -> addStudent());

        resetBtn.addActionListener(e -> clearFields());

        deleteBtn.addActionListener(e -> deleteStudent());

        searchBtn.addActionListener(e -> searchStudent());

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void addLabel(String text,int x,int y){
        JLabel label = new JLabel(text);
        label.setBounds(x,y,120,25);
        add(label);
    }

    private JTextField createField(int x,int y){
        JTextField tf = new JTextField();
        tf.setBounds(x,y,180,25);
        add(tf);
        return tf;
    }

    private void addStudent() {

        if(txtName.getText().trim().isEmpty()
                || txtId.getText().trim().isEmpty()) {

            JOptionPane.showMessageDialog(this,
                    "Name and ID required");
            return;
        }

        String gender =
                maleBtn.isSelected() ? "Male" : "Female";

        Object[] row = {
                txtName.getText(),
                txtId.getText(),
                txtGrade.getText(),
                txtDob.getText(),
                gender,
                txtContact.getText(),
                txtEmail.getText()
        };

        model.addRow(row);

        saveData();

        clearFields();
    }

    private void clearFields() {

        txtName.setText("");
        txtId.setText("");
        txtGrade.setText("");
        txtDob.setText("");
        txtContact.setText("");
        txtEmail.setText("");

        maleBtn.setSelected(false);
        femaleBtn.setSelected(false);
    }

    private void deleteStudent() {

        int row = table.getSelectedRow();

        if(row >= 0){

            model.removeRow(row);
            saveData();
        }
    }

    private void searchStudent() {

        String id = txtSearch.getText();

        for(int i=0;i<model.getRowCount();i++){

            if(model.getValueAt(i,1)
                    .toString().equals(id)) {

                table.setRowSelectionInterval(i,i);

                JOptionPane.showMessageDialog(this,
                        "Student Found");

                return;
            }
        }

        JOptionPane.showMessageDialog(this,
                "Student Not Found");
    }

    private void saveData() {

        try {

            BufferedWriter bw =
                    new BufferedWriter(
                            new FileWriter("students.txt"));

            for(int i=0;i<model.getRowCount();i++) {

                for(int j=0;j<model.getColumnCount();j++) {

                    bw.write(model.getValueAt(i,j).toString());

                    if(j<model.getColumnCount()-1)
                        bw.write(",");
                }

                bw.newLine();
            }

            bw.close();

        } catch(Exception e){
            e.printStackTrace();
        }
    }

    private void loadData() {

        try {

            File file = new File("students.txt");

            if(!file.exists())
                return;

            BufferedReader br =
                    new BufferedReader(
                            new FileReader(file));

            String line;

            while((line=br.readLine())!=null){

                model.addRow(line.split(","));
            }

            br.close();

        } catch(Exception e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(
                StudentManagementSystem::new
        );
    }
}
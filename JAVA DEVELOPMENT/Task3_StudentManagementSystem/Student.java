public class Student {

    private String name;
    private String id;
    private String grade;
    private String dob;
    private String gender;
    private String contact;
    private String email;

    public Student(String name, String id, String grade,
                   String dob, String gender,
                   String contact, String email) {

        this.name = name;
        this.id = id;
        this.grade = grade;
        this.dob = dob;
        this.gender = gender;
        this.contact = contact;
        this.email = email;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public String getGrade() {
        return grade;
    }

    public String getDob() {
        return dob;
    }

    public String getGender() {
        return gender;
    }

    public String getContact() {
        return contact;
    }

    public String getEmail() {
        return email;
    }
} 
from flask import Flask, render_template, redirect, url_for, request

from employee import Employee

employees = []

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def employee_page():
    if request.method == "POST":
        new_employee_id = request.form.get("employee-id", "")
        new_employee_first_name = request.form.get("employee-first-name", "")
        new_employee_last_name = request.form.get("employee-last-name", "")

        new_employee = Employee(id=new_employee_id,
                                first_name=new_employee_first_name,
                                last_name=new_employee_last_name)
        employees.append(new_employee)

        return redirect(url_for("employee_page"))

    # test_employee = Employee(id=33,
    #                         first_name="Test",
    #                         last_name="User")
    # employees.append(test_employee)
    return render_template("index.html", employees=employees)


if __name__ == "__main__":
    app.run(debug=True)     # run in debug
    # app.run()

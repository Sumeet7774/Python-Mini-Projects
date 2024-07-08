class Employee
{
	String eName;
	int basicSalary;
	static int employeeCount = 0;

	// default constructor
	public Employee()
	{
		this.eName = " ";
		this.basicSalary = 0;
	}

	// Overloaded Constructor
	public Employee(String name, int bs)
	{
		this.eName = name;
		this.basicSalary = bs;
		employeeCount++;
	}

	// copy constructor
	public Employee(Employee e)
	{
		this.eName = e.eName;
        	this.basicSalary = e.basicSalary;
		employeeCount++;
	}


	// Getter and setter methods
	public String getName()
	{
		return eName;
	}

	public void setName(String eName)
	{
		this.eName = eName;
	}
	
	public int getBasicSalary()
	{
		return basicSalary;
	}

	public void setBasicSalary(int basicSalary)
	{
		this.basicSalary = basicSalary;
	}

	public int getNetIncome()
	{
		int deductions = 1000;

		return basicSalary - deductions;
	}
	
	public void printEmployeeDetails()
	{
		System.out.println("Name: " + eName);
		System.out.println("Salary: " + basicSalary);
		System.out.println("Net Income: " + getNetIncome());
	}

	public static int countEmployees() 
	{
		return employeeCount;
	}
}

class SalesManager extends Employee 
{
	int salesAmount;

	public SalesManager()
	{
		super();
		this.salesAmount = 0;
	}
	
	public SalesManager(String name, int bs, int sa)
	{
		super(name,bs);
		this.salesAmount = sa; 
	}

	@Override
	public void printEmployeeDetails()
	{
		super.printEmployeeDetails();
		System.out.println("Sales Amount: " + salesAmount);
	}

	@Override
	public int getNetIncome()
	{
		int bonus = salesAmount * 5;

		return super.getNetIncome() + bonus;
	}
}

public class PayrollManagementSystem
{
	public static void main(String args[])
	{
		Employee emp1 = new Employee("Sumeet",50000);
		Employee emp2 = new Employee("Jimit",80000);
	
		SalesManager sl1 = new SalesManager("Vishal",50000, 5000);
		SalesManager sl2 = new SalesManager("Yash",60000,5000);

		emp1.printEmployeeDetails();
		System.out.println();
		emp2.printEmployeeDetails();
		System.out.println();

		sl1.printEmployeeDetails();
		System.out.println();
		sl2.printEmployeeDetails();
		System.out.println();

		int totalEmployee = Employee.countEmployees();
		System.out.println("Total number of employee: " + totalEmployee);
		System.out.println();

	}

}
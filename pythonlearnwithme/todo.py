def task():
    tasks=[]
    print("--------------------WELCOME TO THE TASK MANAGEMENT APP--------------------")

    total_task=int(input("Enter how many task yoou want to add :"))
    for i in range(1,total_task+1):
        task_name=input(f"Enter task{i} = ")
        tasks.append(task_name)
    
    print(f"Today's Task are\n{tasks}")


    while True:
        operation=int(input("Enter 1.Add \n 2.Update \n 3.Delete \n 4.View \n 5.Exit \n"))
        if operation==1 :
            add=input("Enter Task you want to add :")
            tasks.append(add)
            print(f"Task {add} has been adding successfully..")

        elif operation==2:
            update_val=input("Enter the task name you want to update :")
            if update_val in tasks:
                up=input("Enter New Task :")
                ind=tasks.index(update_val)
                tasks[ind]=up
                print(f"Updated task {up}")

        elif  operation==3:
            delete_val=input("Enter the task name you want to delete :")
            if delete_val in tasks:
                ind =tasks.index(delete_val)
                del tasks[ind]
                print(f"task {delete_val} has been delete...")

        elif operation==4:
            print(f"Total tasks ={tasks}")

        elif operation==5:
            print("Closing the program...")
            print("..............THANK YOU.................")
            break 
        else:
            print("Invalid number!! please enter 1-5 number.")      
            print("..............THANK YOU.................")

task()
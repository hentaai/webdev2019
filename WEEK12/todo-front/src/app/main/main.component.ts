import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service'
import { ITaskList, ITask } from '../shared/models/models' 

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public task_lists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public loading = false;
  public name: any;
  public taskName: any;
  public created_at: any;
  public due_on: any;
  public status: any;
  public task_list: any;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
  	  this.task_lists = res;
      setTimeout(() => {
        this.loading = true;
      }, 2000);
    });
  }

  getTasks(task_list: ITaskList) {
    this.provider.getTasks(task_list).then(res => {
      this.tasks = res;
    });
  }

  updateTaskList(task_list: ITaskList){
    this.provider.updateTaskList(task_list).then(res =>
      console.log(task_list.name + 'updated'));
  }

  deleteTaskList(task_list: ITaskList) {
    this.provider.deleteTaskList(task_list.id).then(res => {
      console.log(task_list.name + 'deleted')
      this.provider.getTaskLists().then(res => {
        this.task_lists = res;
      }, error => {
        console.log(error);
      });

    });
  }

  createTaskList() {
    if (this.name !== '') {
      this.provider.createTaskList(this.name).then(res => {
        this.name = '';
        this.task_lists.push(res);
      });
    }
  }

  createTask() {
    if (this.name !== '') {
      this.provider.createTask(this.taskName, this.created_at, this.due_on, this.status, this.task_list).then(res => {
        this.taskName = '';
      });
    }
  }
}

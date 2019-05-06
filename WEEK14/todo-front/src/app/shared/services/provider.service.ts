import { Injectable } from '@angular/core';
import { MainService } from './main.service'
import { HttpClient } from '@angular/common/http'
import {ITaskList, ITask, IAuth} from '../models/models'
import DateTimeFormat = Intl.DateTimeFormat;

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]> {
    return this.get('http://127.0.0.1:8000/api/task_lists/', {})
  }

  getTasks(task_list: ITaskList, suffix: any): Promise<ITask[]> {
    return this.get(`http://127.0.0.1:8000/api/task_lists/${task_list.id}/tasks/` + suffix, {});
  }

  createTask(name: string, created_at: Date, due_on: Date, status: string, task_list: number): Promise<ITask> {
    return this.post(`http://127.0.0.1:8000/api/task_lists/${task_list}/tasks/`, {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status,
      task_list: task_list
    });
  }

  createTaskList(name: string): Promise<ITaskList> {
    return this.post('http://127.0.0.1:8000/api/task_lists/', {
      name: name
    });
  }

  updateTaskList(task_list: ITaskList): Promise<ITaskList
    >{
    return this.put(`http://127.0.0.1:8000/api/task_lists/${task_list.id}/`, {
      name: task_list.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://127.0.0.1:8000/api/task_lists/${id}`, {});
  }

  auth(username: any, password: any): Promise<IAuth>{
    return this.post(`http://127.0.0.1:8000/api/login/`, {
      username: username,
      password: password
    })
  }

  logout(): Promise<any>{
    return this.post('http://127.0.0.1:8000/api/logout/', {

    })
  }
}

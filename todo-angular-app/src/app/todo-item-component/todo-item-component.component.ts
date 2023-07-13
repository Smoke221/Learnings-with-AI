import { Component, Input } from '@angular/core';
import { Todo } from '../todo';
import { TodoService } from '../todo.service';

@Component({
  selector: 'app-todo-item-component',
  templateUrl: './todo-item-component.component.html',
  styleUrls: ['./todo-item-component.component.css'],
})

export class TodoItemComponentComponent {
  @Input() todo: Todo;

  constructor(private todoService: TodoService) {}

  markAsCompleted(todo: Todo) {
    this.todoService.updateTodo(todo.id, { completed: todo.completed });
  }

  deleteTodo(todo: Todo) {
    this.todoService.deleteTodo(todo.id);
  }
}

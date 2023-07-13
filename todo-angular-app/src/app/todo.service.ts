import { Injectable } from '@angular/core';
import { Todo } from './todo';

@Injectable({
  providedIn: 'root',
})
export class TodoService {
  private todos: Todo[] = [];

  getTodos(): Todo[] {
    return this.todos;
  }

  createTodo(todo: Todo) {
    todo.id = this.todos.length + 1;
    this.todos.push(todo);
  }

  updateTodo(id: number, changes: Partial<Todo>) {
    const todo = this.todos.find((t) => t.id === id);
    if (todo) {
      Object.assign(todo, changes);
    }
  }

  deleteTodo(id: number) {
    const index = this.todos.findIndex((t) => t.id === id);
    if (index !== -1) {
      this.todos.splice(index, 1);
    }
  }
}

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TodoListComponentComponent } from './todo-list-component/todo-list-component.component';
import { TodoItemComponentComponent } from './todo-item-component/todo-item-component.component';
import { CreateTodoComponentComponent } from './create-todo-component/create-todo-component.component';

@NgModule({
  declarations: [
    AppComponent,
    TodoListComponentComponent,
    TodoItemComponentComponent,
    CreateTodoComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

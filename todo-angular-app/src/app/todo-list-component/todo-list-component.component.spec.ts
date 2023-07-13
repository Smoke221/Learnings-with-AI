import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TodoListComponentComponent } from './todo-list-component.component';

describe('TodoListComponentComponent', () => {
  let component: TodoListComponentComponent;
  let fixture: ComponentFixture<TodoListComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TodoListComponentComponent]
    });
    fixture = TestBed.createComponent(TodoListComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

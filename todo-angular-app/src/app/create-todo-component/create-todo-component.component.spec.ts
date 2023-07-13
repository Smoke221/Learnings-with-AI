import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateTodoComponentComponent } from './create-todo-component.component';

describe('CreateTodoComponentComponent', () => {
  let component: CreateTodoComponentComponent;
  let fixture: ComponentFixture<CreateTodoComponentComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateTodoComponentComponent]
    });
    fixture = TestBed.createComponent(CreateTodoComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

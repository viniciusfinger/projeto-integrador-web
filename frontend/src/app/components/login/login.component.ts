import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  imports: [CommonModule, FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
    onCadastrar(){ 
    this.isNewLogin = true;
  }
    onLogin(){
    this.isNewLogin = false;
    }
    manterConectado: string = "";
    username: string = "";
    password: string = "";
    isNewLogin: boolean = false;
    nome: string = "";
}

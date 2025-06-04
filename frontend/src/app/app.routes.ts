import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StatusComponent } from './components/status/status.component';
import { LoginComponent } from './components/login/login.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'status', component: StatusComponent },
    { path: 'login', component: LoginComponent },
    { path: '', redirectTo: 'home', pathMatch: 'full' },
    { path: '**', redirectTo: 'home' }
];

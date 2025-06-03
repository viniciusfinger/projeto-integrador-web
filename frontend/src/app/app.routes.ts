import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StatusComponent } from './components/status/status.component';

export const routes: Routes = [
    { path: 'home', component: HomeComponent },
    { path: 'status', component: StatusComponent },
    { path: '', redirectTo: 'home', pathMatch: 'full' },
];

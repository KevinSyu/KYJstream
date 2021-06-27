import { Component } from '@angular/core';
import { MatDrawerToggleResult } from '@angular/material/sidenav';
import { MatSidenav } from '@angular/material/sidenav/sidenav';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  registerPage: boolean = false;
  searchPage: boolean = false;
  errlogPage: boolean = false;
  page = [this.registerPage,
  this.searchPage,
  this.errlogPage];
  title: string = 'KYJStream';

  toggleSideNav(sideNav: MatSidenav) {
    // sideNav.toggle().then((result: MatDrawerToggleResult) => {
    //   console.log(result);
    //   console.log(`選單狀態：${result}`);
    // });
  }

  changePage(num: number) {
    for (let x = 0; x < this.page.length; x++) {
      this.page[x] = false;
    }
    this.page[num] = true;
  }

}

import { Component, OnInit, ViewChild } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatSort } from '@angular/material/sort';

@Component({
  selector: 'app-errlog-page',
  templateUrl: './errlog-page.component.html',
  styleUrls: ['./errlog-page.component.scss']
})
export class ErrlogPageComponent implements OnInit {
  @ViewChild('sortTable') sortTable!: MatSort;
  @ViewChild(MatPaginator, { static: true }) paginator!: MatPaginator;

  logData = new MatTableDataSource<any>();
  totalCount!: number;

  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void { 
    this.getLogs();
  }

  getLogs() {
    this.httpClient.get<any>('http://localhost:8888/kyj_stream/logs').subscribe(data => {
      this.logData = new MatTableDataSource<any>(data.data.logs);
      this.logData.paginator = this.paginator;
      this.logData.sort = this.sortTable;
      this.totalCount = data.data.logs.length;
    })
  }
}

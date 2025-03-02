// albums.component.ts
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AlbumsService } from '../services/albums.service';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit {
  albums: any[] = [];
  loading = false;
  error = false;

  constructor(
    private albumsService: AlbumsService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loading = true;
    this.albumsService.getAlbums().subscribe(
      (data) => {
        this.albums = data;
        this.loading = false;
      },
      (error) => {
        console.error('Error fetching albums:', error);
        this.error = true;
        this.loading = false;
      }
    );
  }

  onSelect(album: any): void {
    this.router.navigate(['/albums', album.id]);
  }
}

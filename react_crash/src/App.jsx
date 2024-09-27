import { useEffect, useState } from "react";
import process from "node:process";
import "./App.css";
import SearchIcon from "./assets/search.svg";
import MovieCard from "./components/MovieCard";

const omdb_api_key = process.env.OMDB_API_KEY;
const API_URL = `http://www.omdbapi.com/?apikey=${omdb_api_key}`;

const App = () => {
  const [movies, setMovies] = useState([]);
  const [search, setSearch] = useState("");
  const searchMovie = async (title) => {
    const resp = await fetch(`${API_URL}&s=${title}`);
    const data = await resp.json();

    setMovies(data.Search);
  };

  useEffect(() => {
    searchMovie("Lord of The Rings");
  }, []);

  return (
    <div className="app">
      <h1>MovieLand</h1>
      <div className="search">
        <input
          placeholder="Search for movies"
          value={search}
          onChange={(event) => {
            setSearch(event.target.value);
          }}
          onKeyPress={(event) => {
            if (event.key === "Enter") {
              searchMovie(search);
            }
          }}
        />
        <img
          src={SearchIcon}
          alt="search"
          onClick={() => {
            searchMovie(search);
          }}
        />
      </div>
      {movies.length > 0 ? (
        <div className="container">
          {movies.map((movie, index) => (
            <MovieCard movie={movie} key={index} />
          ))}
        </div>
      ) : (
        <div className="empty">
          <h2>No movies found</h2>
        </div>
      )}
    </div>
  );
};

export default App;

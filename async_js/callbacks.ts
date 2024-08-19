#!/usr/bin/node
type Post = {
  title: string;
  body: string;
};

const posts: Post[] = [
  { title: "Post one", body: "This is post 1" },
  { title: "Post two", body: "This is post 2" },
];

function getPosts(): undefined {
  setTimeout(() => {
    let output: string = "";
    posts.forEach((post) => {
      output += `${post.title}`;
      console.log(output);
      console.log("Done");
    });
  }, 1000);
}

function createPost(post: Post, callback): undefined {
  setTimeout(() => {
    posts.push(post);
    callback();
  }, 2000);
}

createPost(
  { title: "Post three", body: "Rich boy Bruce Wayne is batman!" },
  getPosts(),
);

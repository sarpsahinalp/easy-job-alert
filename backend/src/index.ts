import { Elysia } from "elysia";
import { fetchToken } from "./auth/token-fetcher";

const GH_TOKEN = fetchToken("gh", ["auth", "token"]);

const app = new Elysia().get("/", () => "Hello Elysia").listen(3000);

console.log(
  `🦊 Elysia is running at ${app.server?.hostname}:${app.server?.port}`
);

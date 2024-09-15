"use client";
import Image from "next/image";
import Link from "next/link";
import { useEffect } from "react";

export default function Home() {
  useEffect(() => {
    function requestNotificationPermission() {
      if ("Notification" in window) {
        // Check if the browser supports notifications
        Notification.requestPermission().then((permission) => {
          if (permission === "granted") {
            console.log("Notification permission granted.");
          } else {
            console.log("Notification permission denied.");
          }
        });
      } else {
        console.log("Notification API not supported.");
      }
    }

    // Call this function when you want to request permission
    requestNotificationPermission();
  }, []);

  return (
    <div className="flex h-full items-center justify-center max-h-screen bg-[radial-gradient(ellipse_at_bottom,_var(--tw-gradient-stops))] from-violet-800 via-violet-950/20 to-black/0">
      <div className="-mt-32 text-center space-y-4">
        <h1 className="text-5xl ">Study better...</h1>
        <h2 className="text-8xl font-bold">right now!</h2>
        <Link href={"/start"} className="">
          <button className="text-2xl mt-10 p-4 px-8 bg-violet-500 rounded-xl">
            Get started
          </button>
        </Link>
      </div>
    </div>
  );
}

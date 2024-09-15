import "./globals.css";
import Link from "next/link";

export const metadata = {
  title: "sessions.ai",
  description: "A better way to study",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={`antialiased`}>
        <div className="flex flex-col h-screen">
          <div className="w-full top-0 left-0 p-8 ">
            <Link href={"/"} className="flex items-center space-x-2">
              <svg
                width="129"
                height="138"
                viewBox="0 0 129 138"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                className="w-8 h-8"
              >
                <path
                  fill-rule="evenodd"
                  clip-rule="evenodd"
                  d="M64.5205 0.565582C80.0212 0.565582 94.252 6.37936 105.376 16.0467L48.9254 50.6398V2.59261C53.9209 1.26725 59.1473 0.565582 64.5205 0.565582ZM110.981 21.5486C122.136 33.8556 129 50.573 129 68.9944C129 72.358 128.769 75.6547 128.328 78.8957L72.8533 44.904L110.981 21.5486ZM126.786 86.859C121.643 107.085 107.99 123.602 90.1486 131.81V64.4169L126.786 86.859ZM82.8758 134.617C77.0617 136.443 70.9013 137.434 64.531 137.434C50.1008 137.434 36.783 132.4 26.047 123.913L82.8863 89.0865L82.8758 134.617ZM20.1175 118.612C7.7547 106.138 0.0410957 88.5296 0.0410957 68.9944C0.0410957 65.6198 0.271979 62.3119 0.723251 59.0598L57.9299 95.4237L20.1175 118.612ZM2.28696 51.063C7.70223 29.8461 22.4893 12.7389 41.6316 5.00945L41.1698 75.7772L2.28696 51.063Z"
                  fill="url(#paint0_linear_1_35)"
                />
                <defs>
                  <linearGradient
                    id="paint0_linear_1_35"
                    x1="64.5205"
                    y1="0.565582"
                    x2="64.5205"
                    y2="137.434"
                    gradientUnits="userSpaceOnUse"
                  >
                    <stop stop-color="white" />
                    <stop offset="0.55" stop-color="#9D00FF" />
                  </linearGradient>
                </defs>
              </svg>
              <h1 className="text-3xl">sessions.ai</h1>
            </Link>
          </div>
          <div className="flex-1 w-full">{children}</div>
        </div>
      </body>
    </html>
  );
}

import type { MouseEvent } from "react";
import { useEffect, useState } from "react";
import Swal from "sweetalert2";

import { is_authenticated } from "../store/auth";
import { Logo, signOutUrl } from "../store/constants";

export default function Header(): JSX.Element {
  const handleSignOutUser = (event: MouseEvent<HTMLButtonElement>): void => {
    event.preventDefault();

    void Swal.fire({
      title: "Are you sure you want to Sign Out?",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Yes, Sign Out!",
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = signOutUrl;
      }
    });
  };

  const [top, setTop] = useState(true);

  useEffect(() => {
    const scrollHandler = (): void => {
      setTop(window.pageYOffset <= 10);
    };

    window.addEventListener("scroll", scrollHandler);
    return (): void => {
      window.removeEventListener("scroll", scrollHandler);
    };
  }, []);

  return (
    <header
      className={`fixed w-full z-30 md:bg-opacity-90 transition duration-300 ease-in-out ${
        !top ? "bg-white backdrop-blur-sm shadow-lg" : ""
      }`}
    >
      <div className="max-w-6xl mx-auto px-5 sm:px-6">
        <div className="flex items-center justify-between h-16 md:h-20">
          <a href="/">
            <div className="flex flex-row">
              <img className="h-8 w-8 sm:h-8" src={Logo} alt="Connect" />
              <div className="pl-2 text-xl text-blue-700">Connect.</div>
            </div>
          </a>

          <nav className="flex flex-grow">
            <ul className="flex flex-grow justify-end flex-wrap items-center">
              {is_authenticated === "true" ? (
                <li>
                  <button
                    type="button"
                    onClick={handleSignOutUser}
                    className="btn-sm text-white bg-red-600 hover:bg-red-700 ml-3"
                  >
                    <span>Sign Out</span>
                    <i className="fa-solid fa-right-from-bracket" />
                  </button>
                </li>
              ) : (
                <>
                  <li>
                    <a
                      href="/accounts/sign-in/"
                      className="font-medium text-gray-600 hover:text-gray-900 px-5 py-3 flex items-center transition duration-150 ease-in-out"
                    >
                      Sign in
                    </a>
                  </li>
                  <li>
                    <a
                      href="/accounts/sign-up/"
                      className="btn-sm text-gray-200 bg-gray-900 hover:bg-gray-800 ml-3"
                    >
                      <span>Sign up</span>
                    </a>
                  </li>
                </>
              )}
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}

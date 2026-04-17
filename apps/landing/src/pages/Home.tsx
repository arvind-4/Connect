import React from "react";

import FeaturesHome from "../components/Features";
import Footer from "../components/Footer";
import Header from "../components/Header";
import HeroHome from "../components/HeroHome";
import Newsletter from "../components/Newsletter";
import Testimonials from "../components/Testimonials";

export default function Home(): JSX.Element {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">
      <Header />
      <main className="flex-grow">
        <HeroHome />
        <FeaturesHome />
        <Testimonials />
        <Newsletter />
      </main>
      <Footer />
    </div>
  );
}

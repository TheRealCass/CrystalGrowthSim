package Phys2010_Final;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

class Particle {
    public double x;
    public double y;

    public Particle(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public void move() {
        Random rand = new Random();
        this.x += rand.nextDouble() * 2 - 1;
        this.y += rand.nextDouble() * 2 - 1;
    }

    public double distanceTo(Particle other) {
        return Math.sqrt(Math.pow(this.x - other.x, 2) + Math.pow(this.y - other.y, 2));
    }
}

class Crystal {
    public List<Particle> particles;

    public Crystal(double seedX, double seedY) {
        this.particles = new ArrayList<Particle>();
        this.particles.add(new Particle(seedX, seedY));
    }

    public void addParticle(Particle particle) {
        this.particles.add(particle);
    }

    public boolean isParticleNear(Particle particle) {
        for (Particle p : this.particles) {
            if (particle.distanceTo(p) < 1) {
                return true;
            }
        }
        return false;
    }
}

public class CrystalGrowth {
    public static Crystal simulateCrystalGrowth(int numParticles) {
        Crystal crystal = new Crystal(0, 0);
        List<Particle> particles = new ArrayList<Particle>();
        Random rand = new Random();
        for (int i = 0; i < numParticles; i++) {
            particles.add(new Particle(rand.nextDouble() * 20 - 10, rand.nextDouble() * 20 - 10));
        }
        while (!particles.isEmpty()) {
            for (int i = 0; i < particles.size(); i++) {
                Particle p = particles.get(i);
                p.move();
                if (crystal.isParticleNear(p)) {
                    crystal.addParticle(p);
                    particles.remove(i);
                    break;
                }
            }
        }
        return crystal;
    }

    public static void main(String[] args) {
        Crystal crystal = simulateCrystalGrowth(100);
        System.out.println(crystal.particles.size());
    }
}
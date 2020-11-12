
Turret Class
============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Turret`




Syntax
------

.. code-block:: csharp

    public class Turret : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.Turret
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Turret


Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Turret
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Turret._ammunition



        :rtype: System.String

        .. code-block:: csharp

            public string _ammunition { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret._baseSprite



        :rtype: System.String

        .. code-block:: csharp

            public string _baseSprite { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret._suppressedFx



        :rtype: System.String

        .. code-block:: csharp

            public string _suppressedFx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret._trackingSpeed



        :rtype: System.Single

        .. code-block:: csharp

            public float _trackingSpeed { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret._turretFlags



        :rtype: Clay.Game.Mod.Entities.TurretFlags

        .. code-block:: csharp

            public TurretFlags _turretFlags { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret.isPingPong



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isPingPong { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret.isSuppressed



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isSuppressed { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret.isTracking



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isTracking { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Turret.visiblePitch



        :rtype: System.Single

        .. code-block:: csharp

            public override float visiblePitch { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Turret
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Turret.Activate(System.Boolean, Attributes, UnityEngine.Vector2, Colony, Team)



        :type colonyPosition: System.Boolean

        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type colony: Colony

        :type team: Team


        .. code-block:: csharp

            public void Activate(bool colonyPosition, Attributes attr, Vector2 atPosition, Colony colony, Team team)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.CanAttack()



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool CanAttack()

    .. dn:method:: Clay.Game.Mod.Entities.Turret.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Turret.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Turret.IsFollowTargetValidCB(Clay.Game.Mod.Entities.Entity, UnityEngine.Vector2)



        :type target: Clay.Game.Mod.Entities.Entity

        :type sourcePosition: UnityEngine.Vector2

        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool IsFollowTargetValidCB(Entity target, Vector2 sourcePosition)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.SetVisiblePitch(System.Single)



        :type value: System.Single


        .. code-block:: csharp

            public override void SetVisiblePitch(float value)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.SpawnTurret(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.Turret

        .. code-block:: csharp

            public static Turret SpawnTurret(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.SpawnTurretLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Turret

        .. code-block:: csharp

            public static Turret SpawnTurretLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Turret.SuppressedBy(Clay.Game.Mod.Entities.Entity, System.Single, System.Boolean, System.Boolean)



        :type attacker: Clay.Game.Mod.Entities.Entity

        :type time: System.Single

        :type effectHandled: System.Boolean

        :type fxHandled: System.Boolean


        .. code-block:: csharp

            public override void SuppressedBy(Entity attacker, float time, bool effectHandled = false, bool fxHandled = false)



